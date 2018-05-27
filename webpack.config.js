var webpack = require("webpack");
var path = require("path");

module.exports = {
  mode: 'development',

  entry: './resources/main.js',
  output: {
    filename: 'app.js',
    path: path.resolve(__dirname, 'tedimg/static'),
    publicPath: '/static/'
  },

  module: {
    rules: [
      {
        test: /\.css$/,
        use: ['style-loader', 'css-loader', 'resolve-url-loader']
      },
      {
        test: /\.(png|woff2?)$/,
        use: ['file-loader']
      }
    ]
  }
}
