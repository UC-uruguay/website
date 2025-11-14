import React from "react";
import LanguageSelector from "./languageSelector";
import styled from "styled-components";
import {Link} from "react-router-dom";
import { HashLink } from 'react-router-hash-link';
import {FormattedMessage} from "react-intl";
import mediaQuery from "styled-media-query";

const Header = () => (
  <div className="ui container">
    <TableContainer>
      <Link to="/">
        <Title>
          <img src="/images/logos/logo.png" alt="logo" className="ui image"/>
        </Title>
      </Link>
      <RightItems>
        <HashLink to="/#service"><Black><FormattedMessage id="header.service"/></Black></HashLink>
        <HashLink to="/#price"><Black><FormattedMessage id="header.price"/></Black></HashLink>
        <a href="mailto:yushi812@gmail.com?subject=Final%20Sequence%20Contact"><Black><FormattedMessage id="header.contact"/></Black></a>
        <div style={{marginTop: "-0.15vw"}}><LanguageSelector/></div>
      </RightItems>
    </TableContainer>
  </div>);

const mediaMobile = mediaQuery.lessThan("medium");

const TableContainer = styled.div`
  display:flex;
  align-items: center;
  justify-content: space-between;
  ${mediaMobile`
    min-height: 10vh;
    display: block;
    font-size:0.9rem;
  `}
  margin-bottom:1rem;
`;
const Title = styled.div`
  display: block;
  width: 25vw;
  ${mediaMobile`width: 100vw;`}
  margin-left: -2vw;
`;
const Black = styled.div`
  color: black;
  margin-right: 4vw;
`;

const RightItems = styled.div`
  display: flex;
  text-align: right;
  color: black;
  ${mediaMobile`justify-content:center;`}
`;
export default Header;
