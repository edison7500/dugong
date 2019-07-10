const MiniCssExtractPlugin = require('mini-css-extract-plugin');
// const CleanWebpackPlugin = require('clean-webpack-plugin');
var path = require("path");
var webpack = require('webpack');


module.exports = {
    context: __dirname,

    entry: './src/js/index.js',

    output: {
        path: path.resolve(__dirname, 'dist'),
        filename: 'js/bundle.js'
    },

    plugins: [
        new MiniCssExtractPlugin({
            // TODO optimize  // seognil LC 2019/06/19
            path: path.resolve(__dirname, 'dist'),
            filename: 'css/[name].css',
            chunkFilename: `css/[id].css`,
        }),
        // new CleanWebpackPlugin(),
        new webpack.ProvidePlugin({
            $: 'jquery',
            jQuery: 'jquery'
        })
    ],

    module: {
        rules: [
            {
                test: /\.jsx?$/,
                exclude: /node_modules/,
            },
            {
                test: /\.(sass|scss|less|css)$/i,

                use: [
                    {loader: MiniCssExtractPlugin.loader},
                    // {loader:"style-loader"},
                    {loader:"css-loader"},
                    {
                        loader:"sass-loader",
                        options: {
                            sourceMap: false
                        }
                    }
                ]
            }
        ]
    },
    //
    resolve: {
        moduleExtensions: [ '-loader' ],
        // modulesDirectories: ['node_modules', ],
        // extensions: ['', '.js', '.json']
    }
}