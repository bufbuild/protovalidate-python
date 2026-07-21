# Copyright (c) 2023-2026 Buf Technologies, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from google.protobuf import descriptor as google_descriptor

# protobuf 7+ removed FieldDescriptor.label / LABEL_REPEATED in favour of is_repeated.
_FieldDescriptorClass = google_descriptor.FieldDescriptor
if hasattr(_FieldDescriptorClass, "is_repeated"):

    def is_repeated(field: google_descriptor.FieldDescriptor) -> bool:
        return field.is_repeated

else:

    def is_repeated(field: google_descriptor.FieldDescriptor) -> bool:
        return field.label == google_descriptor.FieldDescriptor.LABEL_REPEATED
