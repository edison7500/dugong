// var path = require('path');
// var BundleTracker = require('webpack-bundle-tracker');
// // var UglifyJsPlugin = require('uglifyjs-webpack-plugin');
//
//
// var config = require("./webpack.base.config");
//
// // config.mode = 'development'
// config.plugins = config.plugins.concat([
//     new BundleTracker({filename: './webpack-stats.json'}),
// ])
//
// module.exports = config;
//
//

// var path = require('path');
const { CleanWebpackPlugin } = require("clean-webpack-plugin");
const BundleTracker = require("webpack-bundle-tracker");
const merge = require("webpack-merge");
var config = require("./webpack.base.config");


module.exports = merge(config, {
	plugins: [
		new CleanWebpackPlugin(),
		new BundleTracker({filename: "./webpack-stats.json"}),
	]
});

