import React from "react";
import styled from "styled-components";

const Footer = () => (
  <Container>
    <div className="ui container center aligned">
      <div style={{color: "#2C3882"}}>Copyright ©CHANT-THROUGH Ltd. All Right Reserved.</div>
    </div>
  </Container>);

const Container = styled.div`
  background-color: #E6CEBF;
  height: 9vh;
  display: flex;
  justify-content: center;
  align-items: flex-end;
  padding-bottom: 1vh;
`;


export default Footer;
