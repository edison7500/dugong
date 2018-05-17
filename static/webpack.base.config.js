var path = require("path")
var BundleTracker = require('webpack-bundle-tracker');
var UglifyJsPlugin = require('uglifyjs-webpack-plugin');

module.exports = {
    context: __dirname,

    entry: './src/js/app.js',

    output: {
        path: path.resolve(__dirname, 'dist'),
        filename: 'bundle-[hash].js'
    },

    plugins: [

    ]

    // module: {
    //     loaders: []
    // },
    //
    // resolve: {
    //     modulesDirectories: ['node_modules', 'bower_components'],
    //     extensions: ['', '.js', '.jsx']
    // }
}