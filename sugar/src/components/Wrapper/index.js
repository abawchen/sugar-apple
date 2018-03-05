import React from 'react';
import styled, { withTheme } from 'styled-components';

@withTheme
export default class Wrapper extends React.Component {
  render () {
    return (
      <StyledMain>
        {this.props.children}
      </StyledMain>
    );
  }
}

const StyledMain = styled.div`
  background-color: ${props => props.theme.primaryDarker};
  width: 100%;
  display: flex;
  flex: 1 1 auto;
  flex-direction: column;
`;
