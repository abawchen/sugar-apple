import React from 'react';
import PropTypes from 'prop-types';
import styled, { withTheme } from 'styled-components';

@withTheme
export default class Logo extends React.Component {
  render () {
    return (
      <StyledWrapper>
        SUGAR APPLE
      </StyledWrapper>
    );
  }
}

const StyledWrapper = styled.div`
  font-size: inherit;
  color: inherit;
  padding: .5rem;
  display: inline-flex;
  align-items: center;

  &:before {
    content: '';
    width: .25em;
    height: .25em;
    margin-right: .5em;
    border-width: .4em;
    border-style: solid;
    border-top-color: ${props => props.theme.primary};
    border-right-color: ${props => props.theme.accent};
    border-bottom-color: ${props => props.theme.accent};
    border-left-color: ${props => props.theme.primaryLighter};
    display: inline-block;
    border-radius: .2em;
  }
`;
