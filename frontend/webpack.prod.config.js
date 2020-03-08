const {CleanWebpackPlugin} = require("clean-webpack-plugin");
const BundleTracker = require("webpack-bundle-tracker");
const UglifyJsPlugin = require("uglifyjs-webpack-plugin");
const OptimizeCSSAssetsPlugin = require("optimize-css-assets-webpack-plugin");
const merge = require("webpack-merge");
let config = require("./webpack.config");

let publicPath = "https://static.jiaxin.im/static/dist/";


module.exports = merge(config, {
  output: {
    publicPath: publicPath,
  },
  optimization: {
    minimizer: [new OptimizeCSSAssetsPlugin({})],
  },
  plugins: [
    new CleanWebpackPlugin(),
    new UglifyJsPlugin({
      sourceMap: false,
    }),
    new BundleTracker({
      filename: "../static/webpack-stats.json",
      relativePath: true
    }),
  ]
});
