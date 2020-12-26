from textwrap import wrap

import pprint


def parse_input(filename):
    input = [l.strip() for l in open(filename, 'r').readlines()]
    raw_rules = input[:input.index('')]
    raw_words = [word for word in input[input.index(''):] if word != '']
    rules = {}
    for raw_rule in raw_rules:
        id, raw_productions = raw_rule.split(':')
        productions = [ p_.strip().split(' ') for p_ in raw_productions.strip().split('|') ]
        rules[id] = productions
    return rules, raw_words

production_to_segment_cache = {}
def build_dictionary(rules, rule_id='0'):
    
    rule = rules[rule_id]

    if ['"a"'] in rule:
        return ['a']
    if ['"b"'] in rule:
        return ['b']

    if rule_id in production_to_segment_cache:
        return production_to_segment_cache[rule_id]

    allowed_word_segments_by_rule = []
    for production in rule:
        allowed_word_segments_by_production = []
        for next_rule in production:
            allowed_word_segments_by_next_rule = build_dictionary(rules, next_rule)
            if len(allowed_word_segments_by_production) == 0:
                allowed_word_segments_by_production = allowed_word_segments_by_next_rule.copy()
            else:
                enhanced_allowed_word_segments_by_production = []
                for segment in allowed_word_segments_by_next_rule:
                    for prefix in allowed_word_segments_by_production:
                        enhanced_allowed_word_segments_by_production.append(prefix + segment)
                allowed_word_segments_by_production = enhanced_allowed_word_segments_by_production.copy()
        allowed_word_segments_by_rule += allowed_word_segments_by_production
    production_to_segment_cache[rule_id] = allowed_word_segments_by_rule
    return allowed_word_segments_by_rule

rules, words = parse_input('19.in')
dictionary = build_dictionary(rules)

valid_words = 0
for word in words:
    if word in dictionary:
        valid_words += 1

print(valid_words)

# looking at the rule set, we observe that we hit the production rules for 8 and 11 directly
# by applying the generating rule 0. the unaltered production rules are:
# 8: 42
# 11: 42 31
# leveraging the build-up cache while generating the dictionary, we take a look at what either
# of these production rules can generated. we observe that production both rules '42' and '31'
# always generate 8-char wide word segments.
# the altered rules look as follows:
# 8: 42 | 42 8
# 11: 42 31 | 42 11 31
# for rule 8, this means that we either terminate with an 8-char wide word segment or continue
# producing 8-char wide word segments using rule 42. for rule 11, we spread out multiple generated
# word segments using rule 42 from multiple generated word segments from rule 31.
# since rule 0 is defined as '0: 8 11', we always end up with a word that uses at least one word
# segment generated from rule 42, followed by at least one word segment generated from rule 31.
# after rule 31 has been used once, no more word segments can be generated using rule 42. as for
# the number of rule invocations, the following holds: 0 < invocations of rule 31 < invocations
# of rule 42.

word_segments_for_42 = production_to_segment_cache['42']
word_segments_for_31 = production_to_segment_cache['31']

valid_words = 0

for word in words:

    segments = wrap(word, 8)

    i = 0

    invocations_of_rule_42 = 0
    invocations_of_rule_31 = 0

    while i < len(segments) and segments[i] in word_segments_for_42:
        invocations_of_rule_42 += 1
        i += 1

    while i < len(segments) and segments[i] in word_segments_for_31:
        invocations_of_rule_31 += 1
        i += 1

    if i == len(segments) and invocations_of_rule_31 < invocations_of_rule_42 and invocations_of_rule_31 > 0:
        # we were able to fully parse the word against the rules.
        # thus, the word is valid.
        valid_words += 1

print(valid_words)