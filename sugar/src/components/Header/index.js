import React from 'react';
import styled, { withTheme } from 'styled-components';

import Container from '../../components/Container';
import Logo from '../Logo';

@withTheme
export default class Header extends React.Component {
  render () {
    return (
      <StyledHeader>
        <Container>
          <Logo/>
        </Container>
      </StyledHeader>
    );
  }
}

const StyledHeader = styled.header`
  font-size: 1.25rem;
  color: ${props => props.theme.light};
  width: 100%;
  height: ${props => props.theme.headerHeight};
  padding: 0 1rem;
  left: 0px;
  top: 0px;
  position: absolute;
  display: flex;
  align-items: center;
  z-index: 1;
`;
