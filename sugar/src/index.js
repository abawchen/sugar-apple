import React from 'react';
import ReactDom from 'react-dom';
import { Provider } from 'mobx-react';
import { AppContainer } from 'react-hot-loader';
import Stores from './stores';
import App from './components/App';

const stores = new Stores();

const render = Component => {
  ReactDom.render(
    <AppContainer>
      <Provider stores={stores}>
        <Component/>
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
