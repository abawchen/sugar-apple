import React from 'react';
import { create } from "jss";
import preset from "jss-preset-default";
import JssProvider from "react-jss/lib/JssProvider";
import createGenerateClassName from "material-ui/styles/createGenerateClassName";
import { ThemeProvider, injectGlobal } from 'styled-components'
import { MuiThemeProvider, createMuiTheme } from 'material-ui/styles';
import { Switch, Route, Link } from 'react-router-dom';

import Header from '../../components/Header';
import Footer from '../../components/Footer';
import HomePage from '../HomePage';

const jss = create(preset());
jss.options.createGenerateClassName = createGenerateClassName;
jss.options.insertionPoint = "insertion-point-jss";

const fontFamily = 'Roboto, Helvetica, "Noto Sans TC", "Microsoft JhengHei", sans-serif';

injectGlobal`
  * {
    box-sizing: border-box;
    position: relative;
  }

  html {
    font-family: ${fontFamily};
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
`

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

const muiTheme = createMuiTheme({
  typography: {
    fontFamily,
  },
});

export default class App extends React.Component {
  render () {
    return (
      <JssProvider jss={jss}>
        <ThemeProvider theme={appTheme}>
          <MuiThemeProvider theme={muiTheme}>
            <Header/>
            <Switch>
              <Route exact path="/" component={HomePage}/>
            </Switch>
            <Footer/>
          </MuiThemeProvider>
        </ThemeProvider>
      </JssProvider>
    );
  }
}
