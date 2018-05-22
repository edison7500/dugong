var path = require("path")
var webpack = require('webpack')

module.exports = {
    context: __dirname,

    entry: './src/js/index.js',

    output: {
        path: path.resolve(__dirname, 'dist'),
        filename: 'js/bundle.js'
    },

    plugins: [
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