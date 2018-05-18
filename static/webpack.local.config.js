var path = require('path');
var BundleTracker = require('webpack-bundle-tracker');
// var UglifyJsPlugin = require('uglifyjs-webpack-plugin');


var config = require("./webpack.base.config");

config.mode = 'development'
config.plugins = config.plugins.concat([
    new BundleTracker({filename: './webpack-stats.json'}),
])

module.exports = config;


