const {CleanWebpackPlugin} = require("clean-webpack-plugin");
const BundleTracker = require('webpack-bundle-tracker');
const MiniCssExtractPlugin = require("mini-css-extract-plugin");
const argv = require("yargs").argv;
const path = require("path");
const webpack = require("webpack");

let debug = argv.mode !== "production";


module.exports = {
  context: __dirname,
  entry: "./index.js",

  output: {
    path: path.resolve(__dirname, "../static/dist"),
    filename: debug ? "js/[name]-bundle.js" : "js/[contenthash:8].min.js",
  },

  plugins: [
    new MiniCssExtractPlugin({
      // path: path.resolve(__dirname, "../static/dist/css"),
      filename: debug ? "[id]-[contenthash].css" : "[contenthash:8].min.css",
      chunkFilename: debug ? "[id].css" : "[id]-[contenthash].min.css",
    }),
    new CleanWebpackPlugin(),
    new BundleTracker({filename: "../static/webpack-stats.json"}),
    new webpack.ProvidePlugin({
      $: "jquery",
      jQuery: "jquery"
    })
  ],

  module: {
    rules: [
      {
        test: /\.jsx?$/i,
        exclude: /node_modules/,
      },
      {
        test: /\.(sa|sc|c)ss$/i,
        use: [
          {loader: MiniCssExtractPlugin.loader},
          {
            loader: "css-loader",
          },
          {
            loader: "postcss-loader",
            options: {
              plugins: function () {
                return [
                  require('autoprefixer')
                ];
              }
            }
          },
          {
            loader: "sass-loader",
            options: {
              sourceMap: debug
            }
          }
        ]
      },
      {
        test: /\.woff(2)?(\?v=[0-9]\.[0-9]\.[0-9])?$/,
        loader: "url-loader?limit=10000&mimetype=application/font-woff"
      },
      {
        test: /\.(png|jpe?g|gif|svg)(\?.*)?$/i,
        loader: 'url-loader',
        options: {limit: 12000}
      },
      {
        test: /\.(ttf|eot|svg)(\?v=[0-9]\.[0-9]\.[0-9])?$/,
        loader: "file-loader"
      }
    ]
  },
  //
  resolve: {
    moduleExtensions: ["-loader"],
  }
};