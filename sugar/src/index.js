import React from 'react';
import ReactDom from 'react-dom';
import { Provider } from 'mobx-react';
import { AppContainer } from 'react-hot-loader';
import { Router, Route } from 'react-router-dom';
import { createBrowserHistory } from 'history';
import Stores from './stores';
import App from './components/App';

const stores = new Stores();
const history = createBrowserHistory();

const render = Component => {
  ReactDom.render(
    <AppContainer warnings={false}>
      <Provider stores={stores}>
        <Router history={history}>
          <Route path="/" component={Component}/>
        </Router>
      </Provider>
    </AppContainer>,
    document.getElementById('root'),
  );
};

render(App);

if (module.hot) {
  module.hot.accept('./components/App', () => {
    render(App);
  });
}
