import 'dart:async';

import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'dart:math';
import 'package:flutter/services.dart';

import './module/ad_bob_service.dart';
import 'package:google_mobile_ads/google_mobile_ads.dart';
import 'questionsAll/ques_tions.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  MobileAds.instance.initialize();
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      title: 'Qizelogo',
      theme: ThemeData(
          brightness: Brightness.dark,
          colorSchemeSeed: const Color(0xff6750a4),
          useMaterial3: true),
      home: const MyHomePage(title: 'Questions'),
    );
  }
}

class MyHomePage extends StatefulWidget {
  const MyHomePage({super.key, required this.title});

  final String title;

  @override
  State<MyHomePage> createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage>
    with SingleTickerProviderStateMixin {
  late AnimationController controller;

  bool op = false;
  bool uniqueNumbersTrue = false;
  int _counter = 0;
  int _end10Scrin = 0;
  int highscore = 0;
  List<int> uniqueNumbers = [];

  Animation<double>? animation;
  late Timer timer;
  double posValue = 0.0;
  double posValueHeight = 0.0;

  BannerAd? _banner;

  final List<Question> _questions = sampledata
      .map(
        (question) => Question(
            id: question['id'],
            question: question['question'],
            options: question['options'],
            answer: question['answer_index']),
      )
      .toList();

  List<Question> get questions => _questions;
  int random = Random().nextInt(sampledata.length);

  void randomNoRepeats() async {
    random = uniqueNumbers[Random().nextInt(uniqueNumbers.length)];
    uniqueNumbers.remove(random);
    uniqueNumbersTrue = true;

    setState(() {
      random;
      uniqueNumbers;
      uniqueNumbersTrue;
      _counter;
      _end10Scrin++;
      highscore;
    });
  }

  void _createBanerAd() async {
    _banner = BannerAd(
      size: AdSize.fullBanner,
      adUnitId: AdMobService.bannerAdUnitId!,
      listener: AdMobService.bannerAdListener,
      request: const AdRequest(),
    )..load();
  }

  trueOdFalse(final context, int index) async {
    final options = questions[random].options;
    final answer = questions[random].answer;
    int questionsLength = questions.length;

    generateTable() {
      if (uniqueNumbersTrue == false) {
        setState(() {
          uniqueNumbers = List<int>.generate(
              questionsLength, (int index) => index,
              growable: true);
        });
      }
    }

    generateTable();
    op = !op;
    if (op == false) randomNoRepeats();
    if (options[answer] == options[index] && op == true) _counter++;
    posValue = posValue == 0.0 ? MediaQuery.of(context).size.width : 0.0;
    posValueHeight = posValueHeight == 0.0 ? 2.0 : 0.0;

    op == true
        ? timer = Timer(const Duration(milliseconds: 300), () {
            generateTable();
            setState(() {
              op = false;
              posValue = 0.0;
              posValueHeight = 0.0;
              randomNoRepeats();
            });
          })
        : timer.cancel();

    if (_end10Scrin >= 9 && op == true) {
      Navigator.push(
          context,
          CupertinoPageRoute(
            builder: (context) => endScrin(index: index, context: context),
          ));
    }

    setState(() {
      op;
      random;
      _counter;
    });
  }

  Widget endScrin({required BuildContext context, required int index}) {
    trueOdFalse(context, index);
    reset();
    return Scaffold(
      appBar: AppBar(title: const Text('Your score is')),
      body: Container(
          width: MediaQuery.of(context).size.width,
          height: MediaQuery.of(context).size.height,
          padding: const EdgeInsets.all(2),
          child: ListView(
            physics: const NeverScrollableScrollPhysics(),
            children: <Widget>[
              Column(
                mainAxisAlignment: MainAxisAlignment.center,
                children: <Widget>[
                  Padding(
                    padding: const EdgeInsets.all(2.0),
                    child: Image.asset('./lib/logoIcon/icon.png',
                        width: 300, height: 300, fit: BoxFit.cover),
                  ),
                  Text(
                    ' highscore' ' $_counter' '/' '10',
                    style: const TextStyle(fontSize: 25),
                  ),
                  FloatingActionButton.extended(
                    onPressed: () async => {
                      HapticFeedback.mediumImpact(),
                      Navigator.pop(context),
                    },
                    label: const Text(
                      'Try again',
                      style: TextStyle(fontSize: 25),
                    ),
                  ),
                ],
              ),
            ],
          )),
    );
  }

  Future<void> reset() async {
    _createBanerAd();
    setState(() {
      uniqueNumbersTrue;
      _end10Scrin = 0;
      _counter = 0;
    });
  }

  @override
  void initState() {
    _createBanerAd();
  }

  @override
  void dispose() {
    controller.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    final options = questions[random].options;
    final answer = questions[random].answer;

    return Scaffold(
      appBar: AppBar(title: const Text('Whose logo is it?')),
      body: ListView.builder(
        physics: const NeverScrollableScrollPhysics(),
        padding: const EdgeInsets.all(8),
        itemCount: options.length,
        itemBuilder: (BuildContext context, int index) {
          SystemChrome.setPreferredOrientations([
            DeviceOrientation.portraitUp,
            DeviceOrientation.portraitDown,
          ]);

          return Container(
              width: MediaQuery.of(context).size.width,
              padding: const EdgeInsets.all(2),
              child: Center(
                child: Column(
                    mainAxisAlignment: MainAxisAlignment.center,
                    children: <Widget>[
                      (index == 0)
                          ? SizedBox(
                              width: MediaQuery.of(context).size.width,
                              height: 2,
                              child: Stack(children: [
                                AnimatedPositioned(
                                    width: posValue,
                                    height: posValueHeight,
                                    duration: const Duration(milliseconds: 300),
                                    curve: Curves.fastOutSlowIn,
                                    child: Container(
                                        color: const Color(0xff6750a4))),
                              ]))
                          : SizedBox(
                              width: MediaQuery.of(context).size.width,
                              height: 2),
                      (index == 0)
                          ? Padding(
                              padding: const EdgeInsets.all(5.0),
                              child: SizedBox(
                                width: 200,
                                height: 200,
                                child: AnimatedSwitcher(
                                  duration: const Duration(milliseconds: 300),
                                  transitionBuilder: (Widget child,
                                      Animation<double> aniamtion) {
                                    return ScaleTransition(
                                        scale: aniamtion, child: child);
                                  },
                                  child: Image.asset(
                                    key: ValueKey<String>('$_end10Scrin'),
                                    questions[random].question.isEmpty
                                        ? questions[4].question
                                        : questions[random].question,
                                    fit: BoxFit.fitWidth,
                                  ),
                                ),
                              ))
                          : const Padding(padding: EdgeInsets.all(5.0)),
                      Column(children: [
                        Container(
                            width: MediaQuery.of(context).size.width / 1.2,
                            height: MediaQuery.of(context).size.height * 0.08,
                            decoration: BoxDecoration(
                              borderRadius: BorderRadius.circular(10),
                            ),
                            child: (FloatingActionButton.extended(
                              onPressed: () async => {
                                HapticFeedback.mediumImpact(),
                                if (uniqueNumbers.isEmpty)
                                  uniqueNumbersTrue = false,
                                trueOdFalse(context, index),
                              },
                              tooltip: options[index],
                              backgroundColor: op == true
                                  ? (options[answer] == options[index]
                                      ? const Color.fromARGB(255, 41, 95, 43)
                                      : const Color.fromARGB(255, 129, 42, 42))
                                  : null,
                              label: Text(options[index],
                                  maxLines: 10,
                                  softWrap: false,
                                  style: TextStyle(
                                    fontSize: 30,
                                    color: Colors.grey[300],
                                  )),
                            )))
                      ]),
                    ]),
              ));
        },
      ),
      bottomNavigationBar: (_banner == null || _end10Scrin >= 10)
          ? Container(
              height: 0,
            )
          : SizedBox(
              height: 52,
              child: AdWidget(ad: _banner!),
            ),
    );
  }
}
