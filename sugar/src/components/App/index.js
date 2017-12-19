import React from 'react';
import { create } from "jss";
import preset from "jss-preset-default";
import JssProvider from "react-jss/lib/JssProvider";
import createGenerateClassName from "material-ui/styles/createGenerateClassName";
import { ThemeProvider, injectGlobal } from 'styled-components'
import { MuiThemeProvider, createMuiTheme } from 'material-ui/styles';
import { Switch, Route, Link } from 'react-router-dom';
import { inject, observer } from 'mobx-react';

import Header from '../Header';
import Home from '../Home';

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
  }
`

const appTheme = {
  // Dimension
  headerHeight: '4rem',
  // Color
  primary: '#39528b',
  secondary: '#ef4b4c',
};

const muiTheme = createMuiTheme({
  typography: {
    fontFamily,
  },
});

@inject('stores')
@observer
export default class App extends React.Component {
  constructor (props) {
    super(props);
  }

  render () {
    let { stores } = this.props;

    return (
      <JssProvider jss={jss}>
        <ThemeProvider theme={appTheme}>
          <MuiThemeProvider theme={muiTheme}>
            <Header/>
            <Switch>
              <Route exact path="/" component={Home}/>
            </Switch>
          </MuiThemeProvider>
        </ThemeProvider>
      </JssProvider>
    );
  }
}
