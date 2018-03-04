import React from 'react';
import PropTypes from 'prop-types';
import styled, { withTheme } from 'styled-components';

@withTheme
export default class Button extends React.Component {
  render () {
    const {
      className,
      value,
      placeholder,
    } = this.props;

    return (
      <StyledWrapper
        className={className}
        type="text"
        value={value}
        placeholder={placeholder}
      />
    );
  }
}

const StyledWrapper = styled.input`
  font-family: inherit;
  font-size: inherit;
  font-weight: inherit;
  color: ${props => props.theme.dark};
  background-color: ${props => props.theme.light};
  border: 1px solid ${props => props.theme.grey};
  outline: none;
  padding: .4em;
  display: inline-flex;
  align-items: center;
  justify-content: center;
`;
