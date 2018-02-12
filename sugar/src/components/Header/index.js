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
        <Logo>SUGAR APPLE</Logo>
      </StyledHeader>
    );
  }
}

const StyledHeader = styled.header`
  width: 100%;
  height: ${props => props.theme.headerHeight};
  background-color: rgba(0, 0, 0, .1);
  padding: 0 1rem;
  left: 0px;
  top: 0px;
  position: absolute;
  display: flex;
  align-items: center;
  z-index: 1;
`;

const Logo = styled.div`
  font-size: 1.25rem;
  color: #ffffff;
  border: 1px solid #ffffff20;
  padding: .5rem 1rem;
`;
