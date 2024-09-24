class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        longest_prefix_length = 0  # To store the maximum length of the common prefix
        prefix_count = {}  # Dictionary to store the count of prefixes in arr1

        # Process the first array and generate prefixes for each number
        for num in arr1:
            num_str = str(num)  # Convert number to string
            current_prefix = ""  # Start with an empty prefix

            # Build prefixes character by character
            for char in num_str:
                current_prefix += char
                # Update the count of occurrences of each prefix
                prefix_count[current_prefix] = prefix_count.get(current_prefix, 0) + 1

        # Process the second array and check for common prefixes
        for num in arr2:
            num_str = str(num)  # Convert number to string
            current_prefix = ""  # Start with an empty prefix

            # Build prefixes character by character
            for char in num_str:
                current_prefix += char

                # Check if the prefix exists in arr1's prefix dictionary
                if current_prefix in prefix_count:
                    # Update the longest common prefix length if necessary
                    longest_prefix_length = max(longest_prefix_length, len(current_prefix))

        return longest_prefix_length