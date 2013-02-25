There are four fields for keeping state of the test.
*****************************************************

1: Selected Tests

    <input name='selected_tests' value='{{ selected_tests }}' />

    This field contains english names of the tests separated by underscore.
    Test information could be extracted from database
    by corresponding english name.

2: Selected Order

    <input name='selected_order' value='{{ selected_order }}' />

    It contains description of sessions order. It consists of
    two characters: either 'mw' or 'wm' (man -> woman -> together or
    woman -> man -> together correspondingly)

3: Current State

    <input name='current_state' value='{{ current_state }}' />

    Information about current state: session and test.
    It could contain only session number (at the begining)
    relative test number (starting from 0).
    , followed by an underscore,
    followed by number: either 0, 1 or 2
    (depending on which section we are in).


4: Current Answers

    <input name='current_answers' value='{{ current_answers }}' />

    Anwswers on the questions is written in the form 0..5
    (which corresponds to -2 -1 0 1 2). All answers are stored consequently:
    section 1 test 1, section 1 test 2, ..., section 2 test 1, section 2 test 2, ...

Example of fields along test progress
*****************************************************

< just started, selecting tests >

    template: beg_tests
    selected_tests: '' -> 'politics_religion'
    selected_order: ''
    current_state: ''
    current_answer: ''

< tests selected, selecting order >

    template: beg_order
    selected_tests: 'politics_religion'
    selected_order: '' -> 'mw'
    current_state: ''
    current_answer: ''

< setting completed, starting first session >

    template: go_session
    selected_tests: 'politics_religion'
    selected_order: 'mw'
    *current_state: '0' -> '0_0'
    current_answer: ''

< seesion identidied, starting first test >

    template: go_test
    selected_tests: 'politics_religion'
    selected_order: 'mw'
    current_state: '0_0' -> '0_1'
    current_answer: '' -> '0000'

< first test completed, starting second test >

    template: go_test
    selected_tests: 'politics_religion'
    selected_order: 'mw'
    current_state: '0_1' -> '0_2'
    current_answer: '0000' -> '0000111'

< second test completed, starting second session >

    template: go_session
    selected_tests: 'politics_religion'
    selected_order: 'mw'
    *current_state: '1' -> '1_0'
    current_answer: '0000111'

< seesion identidied, starting first test >

    template: go_test
    selected_tests: 'politics_religion'
    selected_order: 'mw'
    current_state: '1_0' -> '1_1'
    current_answer: '0000111' -> '00001114444'

< first test completed, starting second test >

    template: go_test
    selected_tests: 'politics_religion'
    selected_order: 'mw'
    current_state: '1_1' -> '1_2'
    current_answer: '00001114444' -> '00001114444555'

< second test completed, starting third session >

    template: go_session
    selected_tests: 'politics_religion'
    selected_order: 'mw'
    *current_state: '2' -> '2_0'
    current_answer: '00001114444555'

< seesion identidied, starting first test >

    template: go_test
    selected_tests: 'politics_religion'
    selected_order: 'mw'
    current_state: '2_0' -> '2_1'
    current_answer: '00001114444555' -> '000011144445552222'

< first test completed, starting second test >

    template: go_test
    selected_tests: 'politics_religion'
    selected_order: 'mw'
    current_state: '2_1' -> '2_2'
    current_answer: '000011144445552222' -> '000011144445552222333'

< second test completed, results >

    template: go_result
    selected_tests: 'politics_religion'
    selected_order: 'mw'
    current_state: '2_2 '
    current_answer: '000011144445552222333'
This file was modified by PyCharm 2.7 for binding GitHub repository