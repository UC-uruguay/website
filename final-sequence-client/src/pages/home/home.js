import React from "react";
import Header from "../../components/header/header";
import {FormattedMessage} from "react-intl";
import styled from "styled-components";
import Footer from "../../components/footer/footer";
import {Link} from "react-router-dom";
import Slider from "react-slick"
import mediaQuery from "styled-media-query";

const Home = () => {
  const settings = {
    dots: true,
    infinite: true,
    speed: 500,
    slidesToShow: 1,
    slidesToScroll: 1,
    autoplay: true,
    autoplaySpeed: 5000,
    arrows: true,
    swipeToSlide: true
  };
  return (
    <div>
      <Header/>
      <div className="ui middle stackable aligned grid container">
        <Row className="row" style={{marginLeft: "4vw"}}>
          <div className="six wide column">
            <Subtitle>
              <FormattedMessage id="home.subtitle"/>
            </Subtitle>
            <LivingProof>
              <FormattedMessage id="menu.livingProof"/>
            </LivingProof>
            <Link to="/living-proof/1">
              <SeeSampleContainer>
                <SeeSample>
                  <FormattedMessage id="home.seeSample"/>
                </SeeSample>
              </SeeSampleContainer>
            </Link>
          </div>
          <div className="nine wide column"><img className="ui fluid image" src="/images/home/shake_hands.png"/></div>
        </Row>
      </div>
      <Service id="service">
        <Title><h2><FormattedMessage id="home.services"/></h2></Title>
        <div className="ui middle aligned stackable grid container">
          <Row className="row center aligned">
            <div className="eight wide centered column">
              <Link to="/living-proof">
                <img className="centered ui image" src="/images/home/livingProof.png"/>
                <Blue><h3><FormattedMessage id="menu.livingProof"/></h3>
                  <LeftAligned><FormattedMessage id="home.livingProof.description1"/></LeftAligned>
                  <LeftAligned><FormattedMessage id="home.livingProof.description2"/></LeftAligned>
                </Blue>
              </Link>
            </div>
          </Row>
          <Row className="row center aligned">
            <div className="eight wide column">
              <Link to="/ai-kaimyou">
                <img className="centered ui image" src="/images/home/brain.png"/>
                <Blue>
                  <h3><FormattedMessage id="menu.kaimyou"/></h3>
                  <LeftAligned><FormattedMessage id="home.kaimyou.description1"/></LeftAligned>
                  <LeftAligned><FormattedMessage id="home.kaimyou.description2"/></LeftAligned>
                </Blue>
              </Link>
            </div>
            <div className="eight wide column">
              <Link to="/online-funeral">
                <img className="centered ui image" src="/images/home/online.png"/>
                <Blue>
                  <h3><FormattedMessage id="menu.funeral"/></h3>
                  <LeftAligned><FormattedMessage id="home.funeral.description1"/></LeftAligned>
                  <LeftAligned><FormattedMessage id="home.funeral.description2"/></LeftAligned>
                </Blue>
              </Link>
            </div>
          </Row>
        </div>
      </Service>
      <Price id="price">
        <div className="ui container">
          <Title><h2><FormattedMessage id="home.price"/></h2></Title>
          <img src="images/home/price.png" className="ui fluid image"/>
        </div>
      </Price>
      <Customers>
        <Title><h2><FormattedMessage id="home.voice"/></h2></Title>
        <Container>
          <Slider {...settings} style={{width: "45vw"}}>
            <Voices>
              <Message><FormattedMessage id="home.customerMessage1"/></Message>
              <Name><FormattedMessage id="home.customer1"/></Name>
            </Voices>
            <Voices>
              <Message><FormattedMessage id="home.customerMessage1"/></Message>
              <Name><FormattedMessage id="home.customer1"/></Name>
            </Voices>
            <Voices>
              <Message><FormattedMessage id="home.customerMessage1"/></Message>
              <Name><FormattedMessage id="home.customer1"/></Name>
            </Voices>
          </Slider>
        </Container>
      </Customers>
      <Footer/>
    </div>
  )
};

const mediaMobile = mediaQuery.lessThan("medium");
const Title = styled.div`
  padding-top: 5vh;
  padding-bottom: 5vh;
  text-align: center;
  color: rgba(44, 56, 130, 0.56);
`;
const Subtitle = styled.div`
  font-size: 1.5rem;
  ${mediaMobile
  `margin-top: 3vh;
   text-align:center;
   `}
`;
const LivingProof = styled.div`
  font-size : 4rem;
  margin-top : 4vh;
  ${mediaMobile`text-align:center;`}
`;
const SeeSample = styled.span`
  background-color: #2C3882;
  color: white;
  font-size: 1.5rem;
  padding:1vh 4vw 1vh 4vw;
`;
const SeeSampleContainer = styled.div`
  margin-top: 5vh;
  ${mediaMobile`text-align:center;`}
`;
const Row = styled.div`
  margin-top: 5vh;
`;
const Service = styled.div`
  background-color: #FDF5EE;
  padding-bottom: 3vh;
`;
const Price = styled.div`
  background-color: #E6CEBF;
  padding-bottom: 3vh;
`;
const LeftAligned = styled.div`
  text-align: left;
`;
const Blue = styled.div`
  color: #2C3882;
`;
const Customers = styled.div`
  padding-bottom: 5vh;
`;
const Voices = styled.div`
  color: #2C3882;
  text-align: center;
`;
const Container = styled.div`
  display: flex;
  justify-content: center;
`;
const Message = styled.div`
  text-align: left;
  font-size: 1.5rem;
  line-height: normal;
  margin-bottom: 4vh;
`;
const Name = styled.div`
  text-align: center;
  font-size: 1.5rem;
  margin-bottom: 1vh;
`;
export default Home;
