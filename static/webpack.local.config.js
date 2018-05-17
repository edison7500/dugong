var path = require('path');
var BundleTracker = require('webpack-bundle-tracker');
var UglifyJsPlugin = require('uglifyjs-webpack-plugin');


var config = require("./webpack.base.config");

config.mode = 'development'
config.plugins = config.plugins.concat([
    new UglifyJsPlugin(),
    new BundleTracker({filename: './webpack-stats.json'}),
])

module.exports = config;


// module.exports = {
//     mode: 'development',
//     entry: './src/js/app.js',
//     output: {
//         path: path.resolve(__dirname, 'dist'),
//         filename: 'bundle-[hash].js'
//     },
//
//     plugins: [
//         new UglifyJsPlugin(),
//         new BundleTracker({filename: './webpack-stats.json'})
//     ]
//
// };

