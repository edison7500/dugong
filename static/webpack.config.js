const path = require('path');
// const webpack = require('webpack');
// const UglifyJsPlugin = require('uglifyjs-webpack-plugin')


module.exports = {
    mode: 'development',
    entry: './src/app.js',
    output: {
        path: path.resolve(__dirname, 'dist'),
        filename: 'editor.js'
    },
    plugins: [
        // new UglifyJsPlugin()
    ]
};
