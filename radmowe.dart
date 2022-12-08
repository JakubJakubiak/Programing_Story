import 'dart:math';
import 'dart:collection';
import 'package:flutter/material.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      home: MyHomePage(),
    );
  }
}

class MyHomePage extends StatefulWidget {
  @override
  _MyHomePageState createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  // Tablica z której losujemy elementy
  var _myArray = [1, 2, 3, 4, 5];

  // Element, który został wylosowany poprzednio
  var _lastElement;

  // Metoda, która losuje element z tablicy
  void _generateRandomElement() {
    // Jeśli wszystkie elementy zostały już wylosowane, to kończymy
    if (_myArray.length == 0) return;

    // Losujemy element z tablicy
    var randomElement = _myArray.toList()..shuffle().first;

    // Jeśli losowany element jest taki sam jak poprzedni, to losujemy ponownie
    if (randomElement == _lastElement) {
      _generateRandomElement();
      return;
    }

    // Wyświetlamy losowany element
    print(randomElement);

    // Zapamiętujemy wylosowany element jako poprzedni
    _lastElement = randomElement;

    // Usuwamy wylosowany element z tablicy
    _myArray.remove(randomElement);
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Flutter Demo'),
      ),
      body: Center(
        child: RaisedButton(
          onPressed: () {
            _generateRandomElement();
          },
          child: Text('Generate Random Element'),
        ),
      ),
    );
  }
}
