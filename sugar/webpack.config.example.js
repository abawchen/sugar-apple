/**
 * Configure Webpack for each environment by using this example file.
 * Name the config file to "webpack.config.dev.js" for development
 * and "webpack.config.prod.js" for production.
 */

var cfg = {
  dist: './dist',
  publicPath: '/',
  webpackDevServerHost: '0.0.0.0',
  webpackDevServerPort: 3001,
};

module.exports = cfg;
