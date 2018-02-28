import React from 'react';
import styled, { withTheme } from 'styled-components';

@withTheme
export default class Main extends React.Component {
  render () {
    return (
      <StyledMain>
        {this.props.children}
      </StyledMain>
    );
  }
}

const StyledMain = styled.main`
  background-color: ${props => props.theme.primaryDarker};
  width: 100%;
  display: flex;
  flex: 1 1 auto;
  flex-direction: column;
`;
