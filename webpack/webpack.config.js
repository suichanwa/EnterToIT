const path = require('path');
const HtmlWebpackPlugin = require('html-webpack-plugin');

module.exports = {
    mode: 'development',
    entry: {
        main:'./src/index.js', 
        analysis: './src/analytics.js'
    }, 
    output: {
        filename: '[name].bundle.js',
        path: path.resolve(__dirname, 'dist')
    }, 
    plugins: [
        new HtmlWebpackPlugin({
            template: './src/index.html'
        })
    ], 
    module: {
        rules: [
            {
                test: /\.css$/,
                use: ['style-loader','css-loader']
            }
        ]
    }
}