#!/bin/sh
find ./workflow/scripts -regex '.*py' -exec black {} \;
