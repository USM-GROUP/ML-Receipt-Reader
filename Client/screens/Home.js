import React from 'react';
import { StyleSheet, Dimensions, ScrollView } from 'react-native';
import { Block, theme } from 'galio-framework';

import { Card } from '../components';
import receipts from '../constants/receipts';
const { width } = Dimensions.get('screen');

class Home extends React.Component {
  renderReceipts = () => {
    return (
      <ScrollView
        showsVerticalScrollIndicator={false}
        contentContainerStyle={styles.receipts}>
        <Block flex>
          <Card item={receipts[0]} horizontal  />
         
            <Card item={receipts[1]} horizontal />
            <Card item={receipts[2]} horizontal />
          
          <Card item={receipts[3]} horizontal />
          <Card item={receipts[4]} horizontal />
        </Block>
      </ScrollView>
    )
  }

  render() {
    return (
      <Block flex center style={styles.home}>
        {this.renderReceipts()}
      </Block>
    );
  }
}

const styles = StyleSheet.create({
  home: {
    width: width,    
  },
  receipts: {
    width: width - theme.SIZES.BASE * 2,
    paddingVertical: theme.SIZES.BASE,
  },
});

export default Home;
