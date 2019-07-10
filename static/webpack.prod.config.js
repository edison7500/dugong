// var path = require('path');
const BundleTracker = require('webpack-bundle-tracker');
const UglifyJsPlugin = require('uglifyjs-webpack-plugin');
const OptimizeCSSAssetsPlugin = require('optimize-css-assets-webpack-plugin');
const merge = require('webpack-merge');
var config = require("./webpack.base.config");


module.exports = merge(config, {
    // output: {
    //     path: path.resolve(__dirname, 'dist'),
    //     filename: 'js/[name]-bundle.js'
    // },
    optimization: {
        minimizer: [new OptimizeCSSAssetsPlugin({})],
    },
    plugins: [
        new UglifyJsPlugin({
            sourceMap: false,
        }),
        new BundleTracker({filename: './webpack-stats.json'}),
    ]
})
