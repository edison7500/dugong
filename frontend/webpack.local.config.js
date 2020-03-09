const {CleanWebpackPlugin} = require("clean-webpack-plugin");
const BundleTracker = require("webpack-bundle-tracker");
const merge = require("webpack-merge");
let config = require("./webpack.config");


module.exports = merge(config, {
  plugins: [
    new CleanWebpackPlugin(),
    new BundleTracker({filename: "../static/webpack-stats.json"}),
  ]
});

