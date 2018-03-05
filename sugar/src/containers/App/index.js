import React from 'react';
import { ThemeProvider, injectGlobal } from 'styled-components'
import { Switch, Route, Link } from 'react-router-dom';

import Wrapper from '../../components/Wrapper';
import Header from '../../components/Header';
import Footer from '../../components/Footer';
import HomePage from '../HomePage';

injectGlobal`
  * {
    box-sizing: border-box;
    position: relative;
  }

  html {
    font-family: Roboto, Helvetica, "Noto Sans TC", "Microsoft JhengHei", sans-serif;
    font-size: 16px;
    height: 100%;
  }

  body {
    min-height: 100%;
    display: flex;
    flex: 1 1 auto;
    flex-direction: column;
  }

  #root {
    width: 100%;
    display: flex;
    flex: 1 1 auto;
    flex-direction: column;
  }
`;

const appTheme = {
  // Dimension
  headerHeight: '4rem',
  // Color
  primary: '#354b5e',
  primaryLighter: '#415c74',
  primaryDarker: '#293a48',
  accent: '#ff4174',
  accentLighter: '#ff638d',
  accentDarker: '#ff1f5b',
  light: '#f5f5f5',
  grey: '#9e9e9e',
  dark: '#212121',
};

export default class App extends React.Component {
  render () {
    return (
      <ThemeProvider theme={appTheme}>
        <Wrapper>
          <Header/>
          <Switch>
            <Route exact path="/" component={HomePage}/>
          </Switch>
          <Footer/>
        </Wrapper>
      </ThemeProvider>
    );
  }
}
