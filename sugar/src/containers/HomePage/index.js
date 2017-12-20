import React from 'react';
import { inject, observer } from 'mobx-react';
import styled, { withTheme } from 'styled-components';

import Main from '../../components/Main';

@inject('stores')
@observer
@withTheme
export default class HomePage extends React.Component {
  constructor (props) {
    super(props);
  }

  render () {
    let { stores } = this.props;

    return (
      <Main>
        Home
      </Main>
    );
  }
}
