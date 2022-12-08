import 'package:flutter/foundation.dart';

import 'package:firebase_auth/firebase_auth.dart';
// import 'package:firebase_admob/firebase_admob.dart';

import 'package:shared_preferences/shared_preferences.dart';
import 'package:flutter/material.dart';
import 'package:http/http.dart';
import 'dart:math';

import './questionsAll/Questions.dart';
import './module/endScrin.dart';

// void main() {
//   runApp(const MyApp());
// }

// class MyApp extends StatelessWidget {
//   const MyApp({super.key});

//   @override
//   Widget build(BuildContext context) {
//     const cc = Color(0xff6750a4);

//     print(context.widget.key);
//     return MaterialApp(
//       title: 'Flutter Demo',
//       theme: ThemeData(
//           // primarySwatch: Colors.blue,
//           colorSchemeSeed: cc,
//           useMaterial3: true),
//       home: const MyHomePage(title: 'Questions'),
//     );
//   }
// }

// class MyHomePage extends StatefulWidget {
//   const MyHomePage({super.key, required this.title});

//   final String title;

//   @override
//   State<MyHomePage> createState() => _MyHomePageState();
// }

// class _MyHomePageState extends State<MyHomePage> {
//   bool op = false;
//   bool ending = false;
//   bool uniqueNumbersTrue = false;
//   int random = 0;
//   int _counter = 0;
//   int? highscore = 0;
//   List<int> uniqueNumbers = [];

//   final List<Question> _questions = sampledata
//       .map(
//         (question) => Question(
//             id: question['id'],
//             question: question['question'],
//             options: question['options'],
//             answer: question['answer_index']),
//       )
//       .toList();

//   List<Question> get questions => _questions;

//   void randomNoRepeats() {
//     random = Random().nextInt(uniqueNumbers.length);
//     random = uniqueNumbers[random];
//     uniqueNumbers.remove(random);

//     uniqueNumbersTrue = true;

//     setState(() {
//       random;
//       uniqueNumbers;
//       uniqueNumbersTrue;
//       _counter;
//     });
//   }

//   Future<void> TrueOdFalse(final context, int index) async {
//     final options = questions[random].options;
//     final answer = questions[random].answer;
//     final questionsLength = questions.length;

//     if (uniqueNumbersTrue == false) {
//       uniqueNumbers = List<int>.generate(questionsLength, (int index) => index,
//           growable: true);
//       uniqueNumbers.remove(0);
//     }

//     op = !op;
//     uniqueNumbers.isEmpty
//         ? EndScrin()
//         : (op == false)
//             ? randomNoRepeats()
//             : null;

//     if (options[answer] == options[index] && op == true) _counter++;

//     SharedPreferences prefs = await SharedPreferences.getInstance();
//     prefs.setInt('highscore', _counter);

//     int? highscore = prefs.getInt('highscore');

//     print('$highscore' " highscore");
//     print('$_counter' " _counter");

//     setState(() {
//       op;
//       ending;
//       random;
//       _counter;
//     });
//   }

//   EndScrin() {
//     if (op == false) ending = true;

//     return Container(
//       width: MediaQuery.of(context).size.width,
//       padding: const EdgeInsets.all(2),
//       child: Column(
//           mainAxisAlignment: MainAxisAlignment.center,
//           children: <Widget>[
//             Hero(
//               tag: 'photo',
//               child: Image.asset(questions[random].question,
//                   width: 400, height: 400, fit: BoxFit.cover),
//             ),
//             FloatingActionButton.extended(
//                 onPressed: Reset,
//                 label: Text('Win ' '$_counter' ' Points' ' $highscore'))
//           ]),
//     );
//   }

//   void Reset() {
//     ending = false;
//     setState(() {
//       ending;
//     });
//   }

//   @override
//   Widget build(BuildContext context) {
//     final options = questions[random].options;
//     final answer = questions[random].answer;

//     return Scaffold(
//         appBar: AppBar(
//           title: Column(
//             mainAxisAlignment: MainAxisAlignment.center,
//             children: const <Widget>[
//               Padding(
//                 padding: EdgeInsets.all(16.0),
//                 child: Text(
//                   'questions',
//                   maxLines: 10,
//                   softWrap: false,
//                 ),
//               ),
//             ],
//           ),
//         ),
//         body: (ending == true)
//             ? EndScrin()
//             : (ListView.builder(
//                 padding: const EdgeInsets.all(8),
//                 itemCount: options.length,
//                 itemBuilder: (BuildContext context, int index) {
//                   return Container(
//                       width: MediaQuery.of(context).size.width,
//                       padding: const EdgeInsets.all(2),
//                       child: Center(
//                         child: Column(
//                           mainAxisAlignment: MainAxisAlignment.center,
//                           children: <Widget>[
//                             index == 0
//                                 ? Hero(
//                                     tag: 'photo',
//                                     child: Padding(
//                                         padding: const EdgeInsets.all(5.0),
//                                         child: Image.asset(
//                                           questions[random].question.isEmpty
//                                               ? questions[0].question
//                                               : questions[random].question,
//                                           width: 200,
//                                           height: 200,
//                                           fit: BoxFit.cover,
//                                         )),
//                                   )
//                                 : const Padding(padding: EdgeInsets.all(5.0)),
//                             Column(children: [
//                               Container(
//                                 width: MediaQuery.of(context).size.width / 2,
//                                 height: MediaQuery.of(context).size.height / 10,
//                                 decoration: BoxDecoration(
//                                   borderRadius: BorderRadius.circular(10),
//                                 ),
//                                 child: (FloatingActionButton.extended(
//                                     onPressed: () =>
//                                         {TrueOdFalse(context, index)},
//                                     tooltip: options[index],
//                                     backgroundColor: op == true
//                                         ? (options[answer] == options[index]
//                                             ? Colors.green
//                                             : Colors.redAccent)
//                                         : null,
//                                     label: Text(options[index],
//                                         maxLines: 10,
//                                         softWrap: false,
//                                         style: Theme.of(context)
//                                             .textTheme
//                                             .headline4))),
//                               ),
//                             ]),
//                           ],
//                         ),
//                       ));
//                 },
//               )));
//   }
// }

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    final cc = Color(0xff6750a4);
    print(context.widget.key);
    return MaterialApp(
      title: 'Flutter Demo',
      theme: ThemeData(
          // primarySwatch: Colors.blue,
          colorSchemeSeed: cc,
          useMaterial3: true),
      home: MyHomePage(title: 'Questions'),
    );
  }
}

class MyHomePage extends StatefulWidget {
  const MyHomePage({required this.title});

  final String title;

  @override
  State<MyHomePage> createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  bool op = false;
  bool ending = false;
  bool uniqueNumbersTrue = false;
  int random = 0;
  int _counter = 0;
  int? highscore = 0;
  List<int> uniqueNumbers = [];

  final List<Question> _questions = Map.fromEntries(sampledata.map(
    (question) => MapEntry(
      question['id'],
      Question(
          id: question['id'],
          question: question['question'],
          options: question['options'],
          answer: question['answer_index']),
    ),
  )) as List<Question>;

  List<Question> get questions => _questions;

  void randomNoRepeats() {
    random = Random().nextInt(uniqueNumbers.length);
    random = uniqueNumbers[random];
    uniqueNumbers.map;

    uniqueNumbersTrue = true;

    setState(() {
      random;
      uniqueNumbers;
      uniqueNumbersTrue;
      _counter;
    });
  }

  Future<void> TrueOdFalse(final context, int index) async {
    final options = questions[random].options;
    final answer = questions[random].answer;
    final questionsLength = questions.length;

    if (uniqueNumbersTrue == false) {
      uniqueNumbers = List<int>.generate(questionsLength, (int index) => index,
          growable: true);
      uniqueNumbers.remove(0);
    }

    op = !op;
    uniqueNumbers.isEmpty
        ? EndScrin()
        : (op == false)
            ? randomNoRepeats()
            : null;

    if (options[answer] == options[index] && op == true) _counter++;

    SharedPreferences prefs = await SharedPreferences.getInstance();
    prefs.setInt('highscore', _counter);

    int? highscore = prefs.getInt('highscore');

    print('$highscore' " highscore");
    print('$_counter' " _counter");

    setState(() {
      op;
      ending;
      random;
      _counter;
    });
  }

  EndScrin() {
    if (op == false) ending = true;
    return Container(
      width: MediaQuery.of(context).size.width,
      padding: const EdgeInsets.all(2),
      child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            Hero(
              tag: 'photo',
              child: Image.asset(questions[random].question,
                  width: 400, height: 400, fit: BoxFit.cover),
            ),
            FloatingActionButton.extended(
                onPressed: Reset,
                label: Text('Win ' '$_counter'),
                icon: Icon(Icons.alarm),
                backgroundColor: Colors.green),
          ]),
    );
  }

  void Reset() {
    setState(() {
      op = false;
      ending = false;
      _counter = 0;
      uniqueNumbersTrue = false;
      randomNoRepeats();
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(widget.title),
        actions: <Widget>[
          IconButton(
            icon: Icon(Icons.close),
            onPressed: () => Navigator.of(context).pop(),
          ),
        ],
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            FutureBuilder<int>(
              future: SharedPreferences.getInstance()
                  .then((prefs) => prefs.getInt('highscore')),
              initialData: 0,
              builder: (context, snapshot) => Text('Highscore: $snapshot.data'),
            ),
            (ending == true)
                ? EndScrin()
                : Hero(
                    tag: 'photo',
                    child: Image.asset(questions[random].question,
                        width: 400, height: 400, fit: BoxFit.cover),
                  ),
            (op == true)
                ? Text(
                    '$_counter',
                    style: Theme.of(context).textTheme.headline4,
                  )
                : Container(),
            ...questions[random]
                .options
                .map((final option) => FloatingActionButton.extended(
                      onPressed: () => TrueOdFalse(context, option.hashCode),
                      label: Text(option),
                      icon: const Icon(Icons.alarm),
                      backgroundColor: Colors.green,
                    )),
          ],
        ),
      ),
    );
  }
}
