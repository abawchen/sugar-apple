import React from 'react';
import { inject, observer } from 'mobx-react';
import styled, { withTheme } from 'styled-components';

import Main from '../../components/Main';
import Dropdown from '../../components/Dropdown';
import TextBox from '../../components/TextBox';
import Button from '../../components/Button';

@inject('stores')
@withTheme
@observer
export default class HomePage extends React.Component {
  onCityChange = (e) => {
    const cityCode = e.target.value;
    this.props.stores.searchStore.changeCity(cityCode);
  }

  onAreaChange = (e) => {
    const area = e.target.value;
    this.props.stores.searchStore.changeArea(area);
  }

  onSearchClick = () => {
    
  }

  render () {
    const {
      searchStore,
    } = this.props.stores;

    const {
      cities,
      city,
      area,
      trends,
    } = searchStore;

    let cityOptions = [];
    if (cities) {
      cityOptions = cities.map(city => ({
        text: city.name,
        value: city.code,
      }));
    }

    let areaOptions = [];
    if (city) {
      areaOptions = city.areas.map(area => ({
        text: area,
        value: area,
      }));
    }

    return (
      <Main>
        <Hero>
          <HeroTitle>
            為您找出不動產交易行情及趨勢
          </HeroTitle>
          <SearchPanel>
            <SearchDropdown
              value={city.code}
              options={cityOptions}
              onChange={this.onCityChange}
            />
            <SearchDropdown
              value={area}
              options={areaOptions}
              onChange={this.onAreaChange}
            />
            <SearchTextBox
              placeholder={'關鍵字（路段、巷弄、門牌號碼）'}
            />
            <SearchButton onClick={this.onSearchClick}>
              搜　尋
            </SearchButton>
          </SearchPanel>
          <TrendList>
          {trends.map((trend, index) => (
            <TrendItem key={index}>
              <TrendItemBackground/>
              <TrendItemData percentage={trend.percentage}>
                <h2>{trend.cityName}<br/> {trend.areaName}</h2>
                <p>{trend.price.toFixed(1)} <span>萬/坪</span></p>
                <p>{trend.percentage.toFixed(1)}<span>%</span></p>
              </TrendItemData>
            </TrendItem>
          ))}
          </TrendList>
        </Hero>
      </Main>
    );
  }
}

const Hero = styled.div`
  width: 100%;
  height:  auto;
  min-height: 100vh;
  background: url(https://i.imgur.com/zQewMh8.jpg);
  background-size: cover;
  background-position: center;
  padding: 1rem;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;

  &:before {
    content: '';
    width: 100%;
    height: 100%;
    background: linear-gradient(
      to top right,
      ${props => props.theme.primary} 40%,
      ${props => props.theme.accent} 100%
    );
    left: 0;
    top: 0;
    position: absolute;
    display: block;
    opacity: .8;
  }
`;

const HeroTitle = styled.h1`
  font-size: 3.2rem;
  font-weight: 800;
  color: ${props => props.theme.light};
  text-align: center;
  letter-spacing: .25rem;
  margin-top: 8rem;
  padding-left: .25rem;

  @media(max-width: 1024px) {
    font-size: 2.8rem;
  }

  @media(max-width: 768px) {
    font-size: 2.5rem;
  }

  @media(max-width: 480px) {
    font-size: 2.3rem;
    margin-top: 5rem;
  }
`;

const SearchPanel = styled.div`
  font-size: 1.15rem;
  text-align: center;
  margin-bottom: 5rem;
  padding: 1rem;
  background-color: ${props => props.theme.primaryDarker}66;

  @media(max-width: 768px) {
    margin-bottom: 3rem;
  }

  @media(max-width: 480px) {
    margin-bottom: 1.5rem;
    padding: .5rem;
  }

  @media(max-width: 360px) {
    font-size: 1rem;
  }
`;

const SearchDropdown = styled(Dropdown)`
  color: ${props => props.theme.dark};
  min-width: 8rem;
  border-color: ${props => props.theme.primaryLighter};
  margin: .25rem;

  @media (max-width: 480px) {
    min-width: calc(50% - .5rem);
  }
`;

const SearchTextBox = styled(TextBox)`
  color: ${props => props.theme.dark};
  min-width: 18.5rem;
  border-color: ${props => props.theme.primaryLighter};
  margin: .25rem;

  @media(max-width: 480px) {
    min-width: calc(100% - .5rem);
  }
`;

const SearchButton = styled(Button)`
  color: ${props => props.theme.light};
  background-color: ${props => props.theme.accent};
  min-width: 6rem;
  border-color: ${props => props.theme.accent};
  margin: .25rem;
  transition: all .2s;

  &:hover {
    box-shadow: 0px 0px 15px 0px ${props => props.theme.accent};
    border-radius: 2px;
  }
`;

const TrendList = styled.div`
  display: flex;
  flex-wrap: wrap;
  justify-content: center;

  @media (max-width: 768px) {
    flex-wrap: nowrap;
    flex-direction: column;
    align-items: center;
  }
`;

const TrendItem = styled.div`
  width: 10rem;
  height: 10rem;
  color:  ${props => props.theme.light};
  margin: 1rem;
  
  &:hover {
    cursor: pointer;

    @media (max-width: 768px) {
      background-color: ${props => props.theme.light}20;
    }
  }

  @media (max-width: 1024px) {
    width: 8rem;
    height: 8rem;
    margin: .5rem;
  }

  @media (max-width: 768px) {
    width: 100%;
    height: auto;
    border: 1px solid ${props => props.theme.light}20;
    margin: .25rem;
    padding: .5rem;
  }
`;

const TrendItemBackground = styled.div`
  width: 100%;
  height: 100%;
  background-color: ${props => props.theme.primaryLighter};
  border: 3.5rem solid ${props => props.theme.primaryDarker};
  border-radius: 50%;
  display: block;
  opacity: .25;
  transition: border-top-color .3s,
    border-right-color .5s,
    border-bottom-color .8s,
    border-left-color 1.2s;

  &:hover {
    border-color: ${props => props.theme.accent};
  }

  @media (max-width: 1024px) {
    border-width: 2.7rem;
  }

  @media (max-width: 768px) {
    display: none;
  }
`;

const TrendItemData = styled.div`
  white-space: nowrap;
  left: 50%;
  top: 50%;
  position: absolute;
  transform: translate(-50%, -50%);
  display: inline-block;
  pointer-events: none;

  @media (max-width: 1024px) {
    display: flex;
    flex-direction: column;
    align-items: center;
  }

  @media (max-width: 768px) {
    left: 0;
    top: 0;
    position: relative;
    transform: none;
    flex-direction: row;
    justify-content: space-between;
  }

  > h2 {
    font-size: .85rem;
    font-weight: 300;
    letter-spacing: 2px;
    margin: 0 0 .25rem 0;

    > br {
      display: none;

      @media (max-width: 1024px) {
        display: inline;
      }

      @media (max-width: 768px) {
        display: none;
      }
    }

    @media (max-width: 768px) {
      font-size: 1rem;
      margin: 0 1rem 0 0;
      display: inline-block;
    }
  }

  > p {
    font-weight: 300;
    margin: .25rem 0;
    display: inline-block;

    > span {
      font-size: .75rem;
      font-weight: 100;

      @media (max-width: 768px) {
        font-size: 1rem;
      }
    }

    &:nth-of-type(1) {
      font-size: 1.2rem;

      @media (max-width: 768px) {
        font-size: 1rem;
      }
    }

    &:nth-of-type(2) {
      font-size: 1.35rem;

      ${props => props.percentage > 0 && `
        color: #6cce99;
      `}
      ${props => props.percentage == 0 && `
        color: #c9cdd8;
      `}
      ${props => props.percentage < 0 && `
        color: #ff756a;
      `}

      margin-left: .5rem;
      display: inline-block;

      @media (max-width: 1024px) {
        margin-left: 0;
      }

      @media (max-width: 768px) {
        font-size: 1rem;
        margin-left: 1rem;
      }
    }
  }
`;
