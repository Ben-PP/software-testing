# Automation Testing in Flutter

In this text I will dive in to the testing capabilities of Flutter. Flutter is a cross-platform application development framework. It offers a way to develop application for IOS, Android, Linux, Windows, MacOS and web from single codebase. Flutter also happens to offer a tools for automation testing out of the box and we will investigate the capabilities of these tools.

## Flutter

As all ready mentioned, Flutter is a cross-platform development framework similar to React Native. It is developed by Google and it is written for Dart programming language. Key selling points of Flutter are its excellent tooling for developers and easy integration with Google products ([flutter.dev](https://flutter.dev/), 2024). Flutter was released back in 2017 and it has been developed and maintained ever since.

## Automation test tooling

Automation test tooling is a set of tools to develop and run automation tests. These tools can either be provided by the programming language/framework or as an additional package by the community. Some times the language provides a low level implementation and then it is expanded by community. For example in JavaScript there is no native tools for testing provided by the JavaScript, but there is still excellent testing solutions available provided by the open source community. On the other hand there is frameworks like Flutter, which provide complete testing tools out of the box.

Tooling which is available for the developer will affect greatly the experience of developing tests. If writing tests requires considerable effort and feels hard or complicated, it will negatively affect the productivity and well being of developers. On the other hand, if developing the tests is pleasant experience, there is a high probability that the test code written will be better quality as the developer does not hate the process.

Big part of the user experience of writing tests is also contributed by how well is the tools documented. The quality of documentation may vary a lot between different tools varying from non existing to very well documented and with provided examples. If the documentation is good, it will be much easier to achieve what you wish.

## Testing tools provided by Flutter

Flutter provides a comprehensive tools for testing your application out of the box. You do not need any third party software or packages to develop and run the tests. Flutter also provides a very well written documentation about testing a Flutter application and basic concepts of testing. They also provide online courses to learn how to write tests in Dart/Flutter.

Tests in Flutter are divided in to 3 different types following common practises in application testing. These are (More commonly used term between brackets):

- Unit tests (Unit tests)
- Widget tests (Integration tests)
- Integration tests (End to End tests)

Just like everywhere else, unit tests in Flutter focus on testing single functions and methods. Widget tests are Flutters counterpart to traditional integration tests. Widget tests are written to test the Widgets which make out the Flutter app. Finally the Integration tests in Flutter are more commonly referenced as End to End tests outside of Flutter.

### Unit testing

Here is a little example of how unit testing is done in flutter. Consider that we have a class `Toggle`.

```dart
class Toggle {
    bool isOn = false;

    void toggle() => isOn = !isOn;
}
```

For this class we could write unit tests like this:

```dart
import 'package:toggle_app/toggle.dart';
import 'package:test/test.dart';

void main() {
    group('Test toggle start, toggling', (){

        test('Starting position should be false', () {
            expect(Toggle().isOn, false);
        });

        test('value should swap', (){
            final myToggle = Toggle();

            myToggle.toggle();

            expect(myToggle.isOn, true);
        })

    });
}
```

As you see, we imported the `test.dart` package, which is provided by Dart team out of the box. We grouped the connected tests together with `group()` function and wrote the tests inside it. Test results are checked using `expect()`. Syntax is very clear and easy to understand and read. The intuitive syntax of tests helps the developers to write better test code and be more productive.

### Widget tests

In Flutter we call component a Widget. As they say "In React, everything is a component.", in Flutter we say "In Flutter, everything is a Widget.". In widget testing we want to test that our widgets work as intended and render what we want.

Here is a simple HelloWorld widget:

```dart
class HelloWorld extends StatelessWidget {
    return Text('Hello World!')
}
```

Now lets look at how we could test this widget.

```dart
import 'package:flutter_test/flutter_test.dart';
import 'package:HelloWorldApp/hello_world.dart';

void main() {
    testWidgets('HelloWorld renders the message', (tester) async {
        await tester.pumpWidget(const HelloWorld());

        final textFinder = find.text('Hello World!');

        expect(textFinder, findsOneWidget);
    });
}
```

Again, we can see that we are able to test our widget very easily with the tools provided by Flutter and Dart team. Syntax is still very readable and simple. The provided tools make testing widgets simple and easy. There is no need to find and learn different third party libraries as everything needed is provided.

### Integration tests

Writing integration tests or end to end tests are again made easy in Flutter. These tests can be run on a real or emulated device and the tools for this are provided by Flutter CLI. The code is basically identical to widget tests, but we will add one line to the `main()` function.

```dart
void main() {
    IntegrationTestWidgetsFlutterBinding.ensureInitialized();

    // Test functions ...
}
```

This will ensure that our app is initialized on the device running the tests. We will likely also use some different methods of the `WidgetTester` class than just the `pumpWidget()`. These include `tap()`, `longPress()`, etc.

## Ease of testing

As Flutter and Dart provides a comprehensive and well documented testing tools, it makes the life of a developer much easier. This is especially important for smaller development teams where there is no dedicated testers. The few developers probably have their hands and minds full from the programming itself and have no time to learn new and complicated tools just for testing.

## Sources

flutter.dev, (2024), https://flutter.dev, Searched 25.11.2024.
