import React from 'react';
import styled, { withTheme } from 'styled-components';

@withTheme
export default class Main extends React.Component {
  constructor (props) {
    super(props);
  }

  render () {
    return (
      <StyledMain>
        {this.props.children}
      </StyledMain>
    );
  }
}

const StyledMain = styled.main`
  display: flex;
  flex: 1 1 auto;
  flex-direction: column;
`;
