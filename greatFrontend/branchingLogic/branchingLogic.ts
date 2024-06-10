/*

Today weʼll be designing a form builder that our ops team will use to configure forms to surface to the user.
Users will answer the form and then submit their responses.

What weʼre looking for
In this exercise weʼll be specifically creating the data models.
We are not implementing the actual form builder right now.
Ideally weʼd like to see a TypeScript file that describes the data structures that weʼll need to power the form builder.
However, feel free to use any strongly typed language youʼre comfortable with.

Initial models
Thereʼs a couple of models that weʼll need initially to support the form:
Questionnaires
Pages
Questions

Requirements
Part1of3
 A questionnaire can have many pages.
 A page can have multiple questions.
 A question can be one of several types. Question types we want to support:
a Yes/no
b Multiple choice single-select
Live Coding Exercise 1
c Multiple choice multi-select d Numerical
e Free text
 Questions support validation that are configurable by the operations team in the frontend.
a Required
b Min length
c Max length
d Minimum value e Maximum value
Part2of3
 Users are able to submit their responses to the form.
 If the form changes, the user responses and the questions stay the same.
 Support the ability to look up responses regardless what the form looked like at the time it was answered.
Part3of3
 Ability to traverse and skip pages based on question responses.
a For instance, from page A, if age < 10 , then go to page B. Else, go to page C.
 Conditional questions. Example: show question B only if question A is answered a certain way.
a For instance, if question A has an answer of 10 , then show question B.
b Complex expressions: if QuestionA AND QuestionB or QuestionC is
answered a certain way, then show QuestionD and QuestionE.
 Conditional validations. Example: require question B only if question A is answered a certain way.

*/

type ComparisonOperator = "<" | ">" | "<=" | ">=" | "==" | "!=";

type SimpleCondition = {
  type: "comparison";
  questionId: Question["id"];
  operator: ComparisonOperator;
  value: string | number | boolean;
};

type CompoundCondition = {
  type: "compound";
  operator: "AND" | "OR";
  conditions: Condition[];
};

type Condition = SimpleCondition | CompoundCondition;

type PageCondition = {
  condition: Condition;
  nextPageId: string;
};

// Questionnaires
type Questionnaire = {
  id: string;
  pages: Page[];
};
// Pages
type Page = {
  id: string;
  questions: Question[];
  nextPageCondition?: PageCondition[];
};
// Questions
// talked about adding composition of BaseQuestion which has required val, and a UUID
// and question extends basequestion so no duplication
type Question =
  | {
      id: string;
      type: "yesno" | "multi-choice-single" | "multi-choice-multi";
      required: boolean;
    }
  | {
      id: string;
      type: "numerical";
      required: boolean;
      minValue: number;
      maxValue: number;
    }
  | {
      id: string;
      type: "freetext";
      required: boolean;
      minLength: number;
      maxLength: number;
    };

type QuestionResponse<T> = {
  questionId: Question["id"];
  value: T;
};

// support submitting questionnaire in its state 'at that time' as a json blob of key value pairs
type FormSubmission = {
  // questionnaire: Questionnaire;
  id: string;
  created_at: string;
  user_id: string;
  responses: Record<Question["id"], QuestionResponse<string>>;
};
