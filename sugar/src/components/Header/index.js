import React from 'react';
import styled, { withTheme } from 'styled-components';

@withTheme
export default class Header extends React.Component {
  constructor (props) {
    super(props);
  }

  render () {
    return (
      <StyledHeader>
        <Logo>SUGAR <span>APPLE</span></Logo>
      </StyledHeader>
    );
  }
}

const StyledHeader = styled.header`
  width: 100%;
  height: ${props => props.theme.headerHeight};
  border-bottom: 1px solid #eeeeee;
  padding: 0 1rem;
  display: flex;
  align-items: center;
`;

const Logo = styled.div`
  font-size: 2rem;
  font-weight: 600;
  color: ${props => props.theme.primary};
  text-shadow: 2px 2px #e0e0e0;

  > span {
    color: ${props => props.theme.secondary};
  }
`;
