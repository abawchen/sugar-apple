import React from 'react';
import styled, { withTheme } from 'styled-components';

import Logo from '../Logo';

@withTheme
export default class Footer extends React.Component {
  render () {
    return (
      <StyledFooter>
        <Logo/>
      </StyledFooter>
    );
  }
}

const StyledFooter = styled.footer`
  font-size: .8rem;
  color: ${props => props.theme.light};
  background-color: ${props => props.theme.primaryDarker};
  width: 100%;
  padding: 1.5rem 1rem;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
`;
