import React from 'react';
import styled, { withTheme } from 'styled-components';

@withTheme
export default class Container extends React.Component {
  render () {
    return (
      <StyledWrapper>
        {this.props.children}
      </StyledWrapper>
    );
  }
}

const StyledWrapper = styled.div`
  width: 100%;
  max-width: 1200px;
  margin: 0 auto;
`;
