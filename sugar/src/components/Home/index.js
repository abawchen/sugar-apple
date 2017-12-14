import React from 'react';
import { inject, observer } from 'mobx-react';

@inject('stores')
@observer
export default class Home extends React.Component {
  constructor (props) {
    super(props);
  }

  render () {
    let { stores } = this.props;

    return (
      <div>
        Home
      </div>
    );
  }
}
