var path = require("path")
var BundleTracker = require('webpack-bundle-tracker');
var UglifyJsPlugin = require('uglifyjs-webpack-plugin');

module.exports = {
    context: __dirname,

    entry: './src/js/index.js',

    output: {
        path: path.resolve(__dirname, 'dist'),
        filename: 'bundle.js'
    },

    plugins: [

    ],

    module: {
        rules: [
            {
                test: /\.jsx?$/,
                // loader: 'babel-loader',
                exclude: /node_modules/,
                // query: {
                //     presets: ['es2015']
                // }
            }
        ]
    },
    //
    // resolve: {
    //     modulesDirectories: ['node_modules', 'bower_components'],
    //     extensions: ['', '.js', '.jsx']
    // }
}