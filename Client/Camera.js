import React from 'react';
import { Camera } from 'expo-camera';
import { View, Text, Dimensions, StyleSheet, TouchableOpacity, Image } from 'react-native';
import * as ImagePicker from 'expo-image-picker';
import * as Permissions from 'expo-permissions';

const deviceHeight = Dimensions.get('window').height;
const deviceWidth = Dimensions.get('window').width;

  //Method to open camera using System's built in camera
  let openCameraAsync = async () => {
    let result = await ImagePicker.requestCameraPermissionsAsync();
    if(result.granted === false){
      alert('Could not get camera permission!');
      return;
    }

    ImagePicker.launchCameraAsync();

  }


export default class CameraClass extends React.Component{
    

    state = {
        hasPermission: null,
        type: Camera.Constants.Type.back,
    }

    async componentDidMount() {
        const { status } = await Permissions.askAsync(Permissions.CAMERA);
        this.setState({ hasPermission: status === 'granted' });
    }

    render(){
        const { hasPermission } = this.state;
        if (hasPermission === null){
            return <View/>
        } else if (hasPermission === false){
            return <Text> No Permission To Access Camera </Text>
        } else {
            return (
                <View>
                  <Camera style={cameraStyle.preview} type={this.state.cameraType}>
                        {/* Image Picker Button */}
                        <View style={styles.topLeftContainer}>
                            <TouchableOpacity>
                            <Image source={require('./menu_icon.png')} style={styles.icon }></Image>

                            <Text style={{ fontSize: 20, color: 'black', alignSelf: 'center'}}>Pick a photo</Text>
                            </TouchableOpacity>

                        </View>

                        {/* Camera Button */}
                        <View>
                            <TouchableOpacity onPress={openCameraAsync}>
                            <Image 
                                source={require('./camera_icon.png')}
                                style={{alignSelf: 'center', width: 100, height: 100, marginBottom: 10}}>
                            </Image>
                            </TouchableOpacity>
                        </View>
                  </Camera>
              </View>
            );
        }//End If

    }

}

const cameraStyle = StyleSheet.create({
    preview: {
      flex: 1,
      backgroundColor: 'transparent',
      width: deviceWidth,
      height: deviceHeight,
      position: 'absolute',
      marginTop: Expo.Constants.statusBarHeight,
      marginBottom: 0,
      top: 0,
      left: 0,
      right: 0,
      bottom: 0,
      //zIndex: 100
      //alignItems: 'center',
      //justifyContent: 'center',
    },
});


const styles = StyleSheet.create({
    container: {
      flex: 1,
      backgroundColor: '#fff',
      //alignItems: 'center',
      justifyContent: 'center',
    },
    topLeftContainer: {
      flex: 1,
      alignItems: 'flex-start',
      justifyContent: 'flex-start',
      top: 10,
      left: 10,
      marginTop: Expo.Constants.statusBarHeight,
    },
    icon: {
      height: 48,
      width: 32,
      maxHeight: '50%',
      maxWidth: '35%',
  
    },
  
    logo: {
      width: 305,
      height: 159,
      marginBottom: 20,
    },
    instructions: {
      color: '#888',
      fontSize: 18,
      marginHorizontal: 15,
      marginBottom: 10,
    },
    button: {
      backgroundColor: 'blue',
      padding: 20,
      borderRadius: 5,
    },
    buttonText: {
      fontSize: 20,
      color: '#fff',
    },
    thumbnail: {
      width: 300,
      height: 300,
      resizeMode: 'contain',
    },
  });
  