import React from 'react';
import styled, { withTheme } from 'styled-components';

@withTheme
export default class Footer extends React.Component {
  constructor (props) {
    super(props);
  }

  render () {
    return (
      <StyledFooter>
        <div>SUGAR APPLE</div>
      </StyledFooter>
    );
  }
}

const StyledFooter = styled.footer`
  font-size: .8rem;
  color: #ffffff;
  background-color: ${props => props.theme.primary};
  width: 100%;
  padding: 2rem 1rem;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
`;
