const MiniCssExtractPlugin = require("mini-css-extract-plugin");
// const CleanWebpackPlugin = require('clean-webpack-plugin');
const argv = require("yargs").argv;
const path = require("path");
const webpack = require("webpack");

var debug = argv.mode != "production";


module.exports = {
	context: __dirname,
	entry: "./app.js",

	output: {
		path: path.resolve(__dirname, "dist"),
		filename: debug ? "js/[name]-bundle.js" : "js/[name]-[hash].js",
	},

	plugins: [
		new MiniCssExtractPlugin({
			path: path.resolve(__dirname, "dist"),
			filename: debug ? "css/[name].css" : "css/[name]-[hash].css",
			chunkFilename: debug ? "css/[id].css" : "css/[id]-[hash].css",
		}),
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
		moduleExtensions: [ "-loader" ],
		// modulesDirectories: ['node_modules', ],
		// extensions: ['', '.js', '.json']
	}
};