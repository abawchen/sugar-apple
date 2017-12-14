import React from 'react';
import { Switch, Route, Link } from 'react-router-dom';
import { inject, observer } from 'mobx-react';

import Home from '../Home';

@inject('stores')
@observer
export default class App extends React.Component {
  constructor (props) {
    super(props);
  }

  render () {
    let { stores } = this.props;

    return (
      <div>
        <Switch>
          <Route exact path="/" component={Home}/>
        </Switch>
      </div>
    );
  }
}
