import React from 'react';
import { create } from "jss";
import preset from "jss-preset-default";
import JssProvider from "react-jss/lib/JssProvider";
import createGenerateClassName from "material-ui/styles/createGenerateClassName";
import { Switch, Route, Link } from 'react-router-dom';
import { inject, observer } from 'mobx-react';

import Home from '../Home';

const jss = create(preset());
jss.options.createGenerateClassName = createGenerateClassName;
jss.options.insertionPoint = "insertion-point-jss";

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
        <Switch>
          <Route exact path="/" component={Home}/>
        </Switch>
      </JssProvider>
    );
  }
}
