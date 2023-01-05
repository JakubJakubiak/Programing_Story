import React, { Component, constructor, useEffect, useState } from "react";
import { Input } from 'react-native-elements';
import {
  StyleSheet,
  Text,
  View,
  Button,
  Image,
  Animated,
  FlatList,
  ActivityIndicator,
} from "react-native";

export default function Poki() {
  const [poki, setPoki] = useState([]);
  const [isLoading, setLoading] = useState(true);
  const [list, setList] = useState("");
  const [filter, setFilter] =useState([]);

  const API_ENDPOINT = 'https://api.pokemontcg.io/v1/cards';

  useEffect(() => {
    fetch(`${API_ENDPOINT}`)
      .then((response) => response.json())
      .then((json) => setPoki(json.cards))
      .catch((error) => console.error(error))
      .finally(() => setLoading(false));
  }, []);

  useEffect(() => {
    setFilter(
      poki.filter((pokis:any) =>
        pokis.name.toLowerCase().includes(list.toLowerCase())
      )
    );
  }, [list, poki]);

  return (
    <View>
    <View>
      <Input placeholder="Search pokis" onChange={(e:any) => setList(e.target.value)}/>
    </View>
    
    {isLoading ? <ActivityIndicator/> : (
      <FlatList 
        data={filter}
        keyExtractor={({ id }, index) => id}
        renderItem={({ item }:any) => {

        return (
        <View>
        <Image
         key={item.id}
         source={{ uri: `${item.imageUrl}`}}
         style={styles.img} 
        />
       </View>
       )
        }}
      />
    )}
    </View> 
  );
}

const styles = StyleSheet.create({
  img: {
    width: 245,
    height: 342,
    margin: 10,
  },
});