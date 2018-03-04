import React from 'react';
import PropTypes from 'prop-types';
import styled, { withTheme } from 'styled-components';

@withTheme
export default class Dropdown extends React.Component {
  render () {
    const {
      className,
      value,
      options,
      onChange,
    } = this.props;

    return (
      <StyledWrapper className={className}>
        <select value={value} onChange={onChange}>
        {options.map(option => 
          <option value={option.value} key={option.value}>
            {option.text}
          </option>
        )}
        </select>
        <i className="material-icons">keyboard_arrow_down</i>
      </StyledWrapper>
    );
  }
}

const StyledWrapper = styled.div`
  font-size: inherit;
  font-weight: inherit;
  color: ${props => props.theme.dark};
  background-color: ${props => props.theme.light};
  border-color: ${props => props.theme.grey};;
  display: inline-flex;
  align-items: center;

  > select {
    font-family: inherit;
    font-size: inherit;
    font-weight: inherit;
    width: 100%;
    color: inherit;
    background-color: inherit;
    border: 1px solid;
    border-color: inherit;
    outline: none;
    padding: .4em 2em .4em .65em;
    -webkit-appearance: none;
    -moz-appearance: none;
    cursor: pointer;
  }

  > i {
    font-size: inherit;
    color: inherit;
    width: 2em;
    height: 100%;
    right: 0;
    position: absolute;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    pointer-events: none;
  }
`;
