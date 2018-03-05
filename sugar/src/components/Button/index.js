import React from 'react';
import PropTypes from 'prop-types';
import styled, { withTheme } from 'styled-components';

@withTheme
export default class Button extends React.Component {
  render () {
    const {
      className,
      children,
      onClick,
    } = this.props;

    return (
      <StyledWrapper className={className} onClick={onClick}>
        {children}
      </StyledWrapper>
    );
  }
}

const StyledWrapper = styled.div`
  font-size: inherit;
  font-weight: inherit;
  color: ${props => props.theme.dark};
  background-color: ${props => props.theme.light};
  border: 1px solid ${props => props.theme.grey};
  padding: .4em .65em;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;

  > * {
    font-size: inherit;
    color: inherit;
  }
`;
